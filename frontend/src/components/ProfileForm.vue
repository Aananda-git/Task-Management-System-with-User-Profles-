<template>
  <div class="container mt-4" style="max-width: 500px">
    <h4>Create New User Profile</h4>
    <form @submit.prevent="submit" enctype="multipart/form-data">
      <input v-model="username" class="form-control mb-2" placeholder="Username" required />
      <input v-model="email" type="email" class="form-control mb-2" placeholder="Email" required />
      <textarea v-model="bio" class="form-control mb-2" placeholder="Bio (optional)" />
      <input type="file" @change="handleFile" class="form-control mb-3" />
      <button class="btn btn-primary w-100">Create Profile</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import api from '../services/api'
import { useRouter } from 'vue-router'

const username = ref('')
const email = ref('')
const bio = ref('')
const picture = ref<File | null>(null)
const router = useRouter()

const handleFile = (e: Event) => {
  const target = e.target as HTMLInputElement
  if (target.files?.length) {
    picture.value = target.files[0]
  }
}

const submit = async () => {
  const formData = new FormData()
  formData.append('username', username.value)
  formData.append('email', email.value)
  formData.append('bio', bio.value)
  if (picture.value) {
    formData.append('profile_picture', picture.value)
  }

  try {
    await api.post('/create-profile/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    alert('Profile created successfully!')
    router.push('/profiles')
  } catch (err: any) {
    alert('Failed to create profile. Make sure email and username are unique.')
    console.error(err)
  }
}
</script>
