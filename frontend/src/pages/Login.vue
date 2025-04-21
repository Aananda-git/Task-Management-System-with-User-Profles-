<template>
  <div class="container mt-5">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" class="form-control mb-2" />
      <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" />
      <button class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import api from '../services/api';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const router = useRouter();

const login = async () => {
  try {
    const res = await api.post('/api-token-auth/', {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem('token', res.data.token);
    router.push('/dashboard');
  } catch {
    alert('Login failed');
  }
};
</script>
