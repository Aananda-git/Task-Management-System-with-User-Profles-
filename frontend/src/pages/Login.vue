<template>
  <div class="container mt-5" style="max-width: 400px">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" class="form-control mb-2" required />
      <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" required />
      <button class="btn btn-primary w-100">Login</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import api from '../services/api'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()

const login = async () => {
  try {
    const res = await api.post('/api-token-auth/', {
      username: username.value,
      password: password.value,
    })
    localStorage.setItem('token', res.data.token)
    router.push('/dashboard')
  } catch (err) {
    alert('Invalid credentials')
  }
}
</script>
