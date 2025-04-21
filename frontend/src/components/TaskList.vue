<template>
  <div>
    <h3>Tasks</h3>

    <div class="mb-2 d-flex gap-2 align-items-center">
      <select class="form-select w-auto" v-model="filter" @change="loadTasks">
        <option value="">All</option>
        <option value="PENDING">Pending</option>
        <option value="IN_PROGRESS">In Progress</option>
        <option value="COMPLETED">Completed</option>
      </select>
      <button class="btn btn-sm btn-secondary" @click="prevPage" :disabled="page <= 1">Previous</button>
      <button class="btn btn-sm btn-secondary" @click="nextPage" :disabled="!hasMore">Next</button>
    </div>

    <ul class="list-group">
      <li v-for="task in tasks" :key="task.id" class="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <strong>{{ task.title }}</strong>
          <br />
          <span>{{ task.description }}</span>
          <br />
          <small>Due: {{ task.due_date }}</small>
        </div>

        <div class="d-flex align-items-center gap-2">
          <select v-model="task.status" @change="updateStatus(task)" class="form-select form-select-sm">
            <option value="PENDING">Pending</option>
            <option value="IN_PROGRESS">In Progress</option>
            <option value="COMPLETED">Completed</option>
          </select>
          <button class="btn btn-sm btn-danger" @click="deleteTask(task.id)">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import api from '../services/api';
import { ref, onMounted } from 'vue';
import type { Task } from '../types';

const tasks = ref<Task[]>([]);
const filter = ref('');
const page = ref(1);
const hasMore = ref(false);

const loadTasks = async () => {
  const res = await api.get('/tasks/', {
    params: {
      search: filter.value,
      page: page.value,
    },
  });
  tasks.value = res.data.results;
  hasMore.value = !!res.data.next;
};

const updateStatus = async (task: Task) => {
  await api.put(`/tasks/${task.id}/`, task);
};

const deleteTask = async (id: number) => {
  if (confirm('Are you sure you want to delete this task?')) {
    await api.delete(`/tasks/${id}/`);
    loadTasks();
  }
};

const nextPage = () => {
  page.value += 1;
  loadTasks();
};

const prevPage = () => {
  if (page.value > 1) {
    page.value -= 1;
    loadTasks();
  }
};

onMounted(loadTasks);
</script>
