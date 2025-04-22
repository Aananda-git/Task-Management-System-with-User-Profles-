<template>
  <div>
    <h4 class="text-primary">User Profiles</h4>
    <div class="row mt-3" v-if="profiles.length">
      <div v-for="profile in profiles" :key="profile.id" class="col-md-4 mb-3">
        <div class="card shadow-sm h-100 border-0 bg-off-white position-relative">
          <!-- Profile Picture on the left side -->
          <div class="d-flex align-items-center">
            <img
              v-if="profile.profile_picture"
              :src="profile.profile_picture"
              class="profile-img rounded-circle border border-white"
              alt="Profile Picture"
            />
            <div class="ml-3">
              <h5 class="card-title text-dark">{{ profile.username }}</h5>
              <p class="card-text text-black">{{ profile.email }}</p>
              <p class="card-text text-secondary" v-if="profile.bio">{{ profile.bio }}</p>
            </div>
          </div>
          <div class="mt-3 d-flex justify-content-between">
            <button @click="editProfile(profile.id)" class="btn btn-warning btn-sm mr-3">Edit</button>
            <button @click="deleteProfile(profile.id)" class="btn btn-danger btn-sm">Delete</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="mt-3 text-muted">No profiles found.</div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

interface Profile {
  id: number
  username: string
  email: string
  bio: string
  profile_picture: string | null
}

const profiles = ref<Profile[]>([])
const router = useRouter()

const fetchProfiles = async () => {
  try {
    const res = await api.get('/profiles/')
    profiles.value = res.data.results || res.data
  } catch (err) {
    console.error('Failed to load profiles:', err)
  }
}

const editProfile = (id: number) => {
  // Navigate to the profile edit route
  router.push({ name: 'EditProfile', params: { id } })
}

const deleteProfile = (id: number) => {
  api.delete(`/profiles/${id}/`)
    .then(() => {
      alert('Profile deleted successfully')
      fetchProfiles() // Refresh the profiles list
    })
    .catch(err => {
      console.error('Failed to delete profile:', err)
    })
}

onMounted(fetchProfiles)
</script>

<style scoped>
/* Custom styling for the profile image */
.profile-img {
  width: 70px;
  height: 70px;
  object-fit: cover;
  border: 2px solid #fff; 
}

/* Off-white background and shadow for the card */
.bg-off-white {
  background-color: #f9f9f9;
}

/* Adjusting margins for profile text */
.ml-3 {
  margin-left: 1rem;
}

/* Styling the buttons with a small gap between them */
.btn-sm {
  padding: 0.3rem 0.8rem;
}

/* Custom font color */
.text-dark {
  color: #000;
}

.text-black {
  color: #000;
}

.text-secondary {
  color: #6c757d; 
}



</style>
