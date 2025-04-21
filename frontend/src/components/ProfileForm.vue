<template>
  <div class="mt-4">
    <h4>Create User Profile</h4>
    <form @submit.prevent="submit" enctype="multipart/form-data">
      <textarea v-model="bio" class="form-control mb-2" placeholder="Bio (optional)" />
      <input type="file" @change="handleFile" class="form-control mb-2" />
      <button class="btn btn-primary">Create Profile</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import api from '../services/api';
import { ref } from 'vue';

const bio = ref<string>('');
const picture = ref<File | null>(null);

const handleFile = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files?.length) {
    picture.value = target.files[0];
  }
};

const submit = async () => {
  const formData = new FormData();
  formData.append('bio', bio.value);
  if (picture.value) {
    formData.append('profile_picture', picture.value);
  }

  await api.post('/profiles/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });

  alert('Profile created!');
  bio.value = '';
  picture.value = null;
};
</script>
