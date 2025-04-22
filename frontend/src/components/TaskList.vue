<template>
  <div>
    <h4 class="text-success">Task List</h4>

    <!-- Task Table -->
    <div v-if="tasks.length" class="table-responsive">
      <table class="table table-bordered mt-3">
        <thead class="table-success">
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
              <button class="btn btn-sm btn-primary me-1" @click="editTask(task)">Edit</button>
              <button class="btn btn-sm btn-danger" @click="task.id !== undefined && deleteTask(task.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination Controls -->
      <div class="d-flex justify-content-center mt-3">
        <nav>
          <ul class="pagination">
            <li class="page-item" :class="{ 'disabled': currentPage === 1 }">
              <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">Previous</a>
            </li>
            <li
              class="page-item"
              :class="{ 'active': currentPage === page }"
              v-for="page in totalPages"
              :key="page"
            >
              <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
            </li>
            <li class="page-item" :class="{ 'disabled': currentPage === totalPages }">
              <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">Next</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>

    <div v-else class="mt-3 text-muted">No tasks available.</div>

    <!-- Success Message -->
    <div v-if="isTaskDeleted" class="alert alert-success mt-3" role="alert">
      Your task has been deleted.
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed } from 'vue'
import api from '../services/api'
import router from '../router'

interface Task {
  id: number
  title: string
  description: string
  status: string
  due_date: string
  assigned_to: string
}

interface Profile {
  id: number
  username: string
}

const tasks = ref<Task[]>([])
const profiles = ref<Profile[]>([])

// Pagination
const currentPage = ref(1)
const tasksPerPage = 5
const totalTasks = ref(0)
const isTaskDeleted = ref(false) // Flag to track task deletion success

const fetchTasks = async () => {
  try {
    const res = await api.get(`/tasks/?page=${currentPage.value}&page_size=${tasksPerPage}`)
    tasks.value = res.data.results || res.data
    totalTasks.value = res.data.count || 0
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
  if (!window.confirm('Are you sure you want to delete this task?')) return
  try {
    await api.delete(`/tasks/${id}/`)
    isTaskDeleted.value = true  // Set the deletion flag to true
    fetchTasks()
    setTimeout(() => {
      isTaskDeleted.value = false // Hide the success message after a short delay
    }, 3000)
  } catch (err) {
    console.error('Failed to delete task:', err)
  }
}

const editTask = (task: Task) => {
  router.push({ name: 'EditTask', params: { id: task.id } })
}

const changePage = (page: number) => {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  fetchTasks()
}

const totalPages = computed(() => Math.ceil(totalTasks.value / tasksPerPage))

onMounted(() => {
  fetchTasks()
  fetchProfiles()
})
</script>
