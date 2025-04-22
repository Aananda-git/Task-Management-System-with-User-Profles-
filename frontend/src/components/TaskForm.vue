<template>
  <div class="container mt-5">
    <h4 class="mb-4 text-center">{{ task.id ? 'Update Task' : 'Create Task' }}</h4>
    <form @submit.prevent="submitTask" class="form-container">
      <!-- Title -->
      <div class="form-group">
        <label for="title" class="font-weight-bold">Title</label>
        <input
          v-model="task.title"
          id="title"
          class="form-control"
          type="text"
          placeholder="Enter task title"
          required
        />
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description" class="font-weight-bold">Description</label>
        <textarea
          v-model="task.description"
          id="description"
          class="form-control"
          placeholder="Enter task description"
          rows="4"
          required
        ></textarea>
      </div>

      <!-- Status -->
      <div class="form-group">
        <label for="status" class="font-weight-bold">Status</label>
        <select v-model="task.status" id="status" class="form-control" required>
          <option value="PENDING">Pending</option>
          <option value="IN_PROGRESS">In Progress</option>
          <option value="COMPLETED">Completed</option>
        </select>
      </div>

      <!-- Due Date -->
      <div class="form-group">
        <label for="due_date" class="font-weight-bold">Due Date</label>
        <input
          v-model="task.due_date"
          id="due_date"
          type="date"
          class="form-control"
          required
        />
      </div>

      <!-- Assigned To -->
      <div class="form-group">
        <label for="assigned_to" class="font-weight-bold">Assigned To</label>
        <select v-model="task.assigned_to" id="assigned_to" class="form-control" required>
          <option value="" disabled>Select a user</option>
          <option v-for="profile in profiles" :key="profile.id" :value="profile.username">
            {{ profile.username }}
          </option>
        </select>
      </div>

      <!-- Save Button -->
      <div class="form-group text-center mt-4">
        <button type="submit" class="btn btn-primary btn-lg px-4">Save Task</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import type { Task, Profile } from '../types'
import router from '../router'
import { useRoute } from 'vue-router'

// Task data
const task = ref<Task>({
  id: 0,
  title: '',
  description: '',
  status: 'PENDING',
  due_date: '',
  assigned_to: '',
})

// Profiles list
const profiles = ref<Profile[]>([])

// Get task ID from route params for editing
const route = useRoute()

const fetchTask = async (id: number) => {
  try {
    const res = await api.get(`/tasks/${id}/`)
    task.value = res.data
  } catch (err) {
    console.error('Failed to fetch task:', err)
  }
}

// Fetch profiles
const fetchProfiles = async () => {
  try {
    const res = await api.get('/profiles/')
    profiles.value = res.data.results || res.data
  } catch (err) {
    console.error('Failed to fetch profiles:', err)
  }
}

// Submit the task
const submitTask = async () => {
  try {
    if (task.value.id) {
      await api.put(`/tasks/${task.value.id}/`, task.value)
      alert('Task updated successfully!')
    } else {
      await api.post('/tasks/', task.value)
      alert('Task created successfully!')
    }
    router.push('/dashboard')
  } catch (err) {
    alert('Failed to save task.')
    console.error(err)
  }
}

// Load task for editing when the component mounts
onMounted(() => {
  if (route.params.id) {
    fetchTask(Number(route.params.id))
  }
  fetchProfiles()
})
</script>

<style scoped>
/* Container width */
.container {
  max-width: 700px; /* Form width limit */
  padding: 0 15px; /* Add padding on the sides */
}

/* Form layout adjustments */
.form-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 3rem; /* Space after the form */
}

.form-group {
  margin-bottom: 1rem;
}

h4 {
  font-size: 1.5rem;
  font-weight: bold;
}

/* Input styling */
.form-control {
  font-size: 1rem;
  padding: 0.8rem;
  border-radius: 0.375rem;
  border: 1px solid #ced4da;
}

/* Textarea styling */
textarea.form-control {
  resize: none;
}

/* Button */
button.btn-primary {
  padding: 1rem;
  width: 100%;
  border-radius: 0.375rem;
  font-size: 1.1rem;
}

button.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

/* Extra responsive adjustments */
@media (max-width: 768px) {
  .container {
    max-width: 100%;
  }

  h4 {
    font-size: 1.3rem;
  }

  button.btn-primary {
    padding: 0.8rem;
    font-size: 1rem;
  }
}
</style>
