<template>
  <div class="container mt-4">
    <h4>Task List</h4>

    <div v-if="tasks.length" class="table-responsive">
      <table class="table table-bordered mt-3">
        <thead class="table-light">
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Status</th>
            <th>Due Date</th>
            <th>Assigned To</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in tasks" :key="task.id">
            <td>{{ task.title }}</td>
            <td>{{ task.description }}</td>
            <td>
              <select v-model="task.status" @change="updateStatus(task)" class="form-select form-select-sm">
                <option value="PENDING">Pending</option>
                <option value="IN_PROGRESS">In Progress</option>
                <option value="COMPLETED">Completed</option>
              </select>
            </td>
            <td>{{ task.due_date }}</td>
            <td>{{ getAssignedUserName(task.assigned_to) }}</td>
            <td>
              <button class="btn btn-danger btn-sm" @click="task.id !== undefined && deleteTask(task.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination -->
      <div class="d-flex justify-content-between align-items-center mt-2">
        <button class="btn btn-outline-secondary" :disabled="page === 1" @click="page--">Previous</button>
        <span>Page {{ page }}</span>
        <button class="btn btn-outline-secondary" @click="page++">Next</button>
      </div>
    </div>

    <div v-else class="mt-3">No tasks available.</div>
  </div>
</template>

<script lang="ts" setup>
import { ref, watchEffect } from 'vue'
import api from '../services/api'
import type { Task, Profile } from '../types'

const tasks = ref<Task[]>([])
const profiles = ref<Profile[]>([])
const page = ref(1)

const fetchTasks = async () => {
  try {
    const res = await api.get(`/tasks/?page=${page.value}`)
    tasks.value = res.data.results || res.data
  } catch (err) {
    console.error('Failed to fetch tasks:', err)
  }
}

const fetchProfiles = async () => {
  try {
    const res = await api.get('/profiles/')
    profiles.value = res.data.results || res.data
  } catch (err) {
    console.error('Failed to fetch profiles:', err)
  }
}

const getAssignedUserName = (username: string) => {
  const user = profiles.value.find(profile => profile.username === username)
  return user ? user.username : username 
}

const updateStatus = async (task: Task) => {
  try {
    await api.put(`/tasks/${task.id}/`, task)
    alert('Status updated!')
  } catch (err) {
    alert('Failed to update status.')
    console.error(err)
  }
}

const deleteTask = async (id: number) => {
  if (!confirm('Are you sure you want to delete this task?')) return
  try {
    await api.delete(`/tasks/${id}/`)
    alert('Task deleted.')
    fetchTasks()
  } catch (err) {
    alert('Failed to delete task.')
    console.error(err)
  }
}

watchEffect(() => {
  fetchTasks()
  fetchProfiles()
})
</script>
