<template>
  <div class="mt-4">
    <h4>Create Task</h4>
    <form @submit.prevent="submit">
      <input v-model="form.title" class="form-control mb-2" placeholder="Title" />
      <textarea v-model="form.description" class="form-control mb-2" placeholder="Description" />
      <input type="date" v-model="form.due_date" class="form-control mb-2" />
      <select v-model="form.status" class="form-select mb-2">
        <option value="PENDING">Pending</option>
        <option value="IN_PROGRESS">In Progress</option>
        <option value="COMPLETED">Completed</option>
      </select>
      <select v-model="form.assigned_to" class="form-select mb-3">
        <option v-for="p in profiles" :key="p.id" :value="p.id">{{ p.user.username }}</option>
      </select>
      <button class="btn btn-success">Submit</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import api from '../services/api';
import { ref, onMounted } from 'vue';
import type { Task, UserProfile } from '../types';

const form = ref<Partial<Task>>({
  title: '',
  description: '',
  due_date: '',
  status: 'PENDING',
  assigned_to: undefined,
});

const profiles = ref<UserProfile[]>([]);

const loadProfiles = async () => {
  const res = await api.get('/profiles/');
  profiles.value = res.data;
};

const submit = async () => {
  await api.post('/tasks/', form.value);
  alert('Task created!');
  form.value = { title: '', description: '', due_date: '', status: 'PENDING' };
};

onMounted(loadProfiles);
</script>
