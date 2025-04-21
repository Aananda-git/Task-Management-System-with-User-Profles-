<template>
  <div class="container mt-4">
    <h4>User Profiles</h4>
    <div class="row mt-3" v-if="profiles.length">
      <div v-for="profile in profiles" :key="profile.id" class="col-md-4 mb-3">
        <div class="card h-100 shadow-sm">
          <img
            v-if="profile.profile_picture"
            :src="profile.profile_picture"
            class="card-img-top"
            alt="Profile Picture"
          />
          <div class="card-body">
            <h5 class="card-title">{{ profile.username }}</h5>
            <p class="card-text"><strong>Email:</strong> {{ profile.email }}</p>
            <p class="card-text" v-if="profile.bio"><strong>Bio:</strong> {{ profile.bio }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="mt-3">No profiles found.</div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import api from '../services/api'

interface Profile {
  id: number
  username: string
  email: string
  bio: string
  profile_picture: string | null
}

const profiles = ref<Profile[]>([])

const fetchProfiles = async () => {
  try {
    const res = await api.get('/profiles/')
    profiles.value = res.data.results || res.data // depends on pagination
  } catch (err) {
    console.error('Failed to load profiles:', err)
  }
}

onMounted(fetchProfiles)
</script>
