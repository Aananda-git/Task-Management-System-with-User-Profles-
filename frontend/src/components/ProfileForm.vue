<template>
  <div class="container mt-5">
    <div class="card shadow-sm">
      <div class="card-body">
        <h5 class="card-title">{{ isEdit ? 'Edit User Profile' : 'Create New User Profile' }}</h5>
        <form @submit.prevent="submit" enctype="multipart/form-data">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input
              id="username"
              v-model="username"
              class="form-control"
              placeholder="Enter your username"
              required
            />
          </div>

          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input
              id="email"
              v-model="email"
              type="email"
              class="form-control"
              placeholder="Enter your email"
              required
            />
          </div>

          <div class="mb-3">
            <label for="bio" class="form-label">Bio</label>
            <textarea
              id="bio"
              v-model="bio"
              class="form-control"
              placeholder="Tell us something about yourself (optional)"
              rows="4"
            ></textarea>
          </div>

          <div class="mb-3">
            <label for="profile-picture" class="form-label">Profile Picture</label>
            <input
              id="profile-picture"
              type="file"
              @change="handleFile"
              class="form-control"
            />
          </div>

          <button class="btn btn-primary w-100 mt-3">
            {{ isEdit ? 'Update Profile' : 'Create Profile' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../services/api'
import router from '../router'

const emit = defineEmits(['submitted'])

const username = ref('')
const email = ref('')
const bio = ref('')
const picture = ref<File | null>(null)
const isEdit = ref(false)
const route = useRoute()

onMounted(async () => {
  if (route.params.id) {
    isEdit.value = true
    try {
      const res = await api.get(`/profiles/${route.params.id}/`)
      const profile = res.data
      username.value = profile.username
      email.value = profile.email
      bio.value = profile.bio || ''
    } catch (err) {
      console.error('Failed to load profile:', err)
    }
  }
})

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
    if (isEdit.value) {
      await api.put(`/profiles/${route.params.id}/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      alert('Profile updated successfully!')
      router.push('/dashboard')
    } else {
      await api.post('/create-profile/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      alert('Profile created successfully!')
      router.push('/dashboard')
    }
    emit('submitted')
  } catch (err: any) {
    alert('Failed to submit profile. Ensure email and username are unique.')
    console.error(err)
  }
}
</script>

<style scoped>
/* Custom styling to enhance form appearance */
.container {
  max-width: 600px;
}
.card {
  border-radius: 10px;
}
.card-body {
  padding: 2rem;
}
</style>
