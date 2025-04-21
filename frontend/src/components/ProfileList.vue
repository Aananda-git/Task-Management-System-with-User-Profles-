<template>
  <div>
    <h3>User Profiles</h3>
    <ul class="list-group">
      <li v-for="profile in profiles" :key="profile.id" class="list-group-item">
        <div class="d-flex justify-content-between align-items-start">
          <div>
            <strong>{{ profile.user.username }}</strong> - {{ profile.bio || 'No bio' }}
            <div v-if="profile.profile_picture">
              <img :src="profile.profile_picture" alt="profile" class="img-thumbnail mt-1" style="max-width: 80px;" />
            </div>
          </div>

          <div class="btn-group">
            <button class="btn btn-sm btn-warning" @click="edit(profile)">Edit</button>
            <button class="btn btn-sm btn-danger" @click="remove(profile.id)">Delete</button>
          </div>
        </div>
      </li>
    </ul>

    <div v-if="editingProfile" class="mt-3">
      <h5>Edit Profile</h5>
      <form @submit.prevent="submitEdit" enctype="multipart/form-data">
        <textarea v-model="editBio" class="form-control mb-2" />
        <input type="file" @change="handleEditFile" class="form-control mb-2" />
        <button class="btn btn-success btn-sm">Update</button>
      </form>
    </div>
  </div>
</template>

<script lang="ts" setup>
import api from '../services/api';
import { ref, onMounted } from 'vue';
import type { UserProfile } from '../types';

const profiles = ref<UserProfile[]>([]);
const editingProfile = ref<UserProfile | null>(null);
const editBio = ref('');
const editPic = ref<File | null>(null);

const loadProfiles = async () => {
  const res = await api.get('/profiles/');
  profiles.value = res.data;
};

const edit = (profile: UserProfile) => {
  editingProfile.value = profile;
  editBio.value = profile.bio || '';
};

const handleEditFile = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files?.length) {
    editPic.value = target.files[0];
  }
};

const submitEdit = async () => {
  if (!editingProfile.value) return;

  const formData = new FormData();
  formData.append('bio', editBio.value);
  if (editPic.value) {
    formData.append('profile_picture', editPic.value);
  }

  await api.put(`/profiles/${editingProfile.value.id}/`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });

  editingProfile.value = null;
  editBio.value = '';
  editPic.value = null;
  loadProfiles();
};

const remove = async (id: number) => {
  if (confirm('Delete this profile?')) {
    await api.delete(`/profiles/${id}/`);
    loadProfiles();
  }
};

onMounted(loadProfiles);
</script>
