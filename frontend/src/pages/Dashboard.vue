<template>
    <div>
      <Navbar />
      <div class="container mt-4">
        <ProfileForm />
        <ProfileList />
        <hr />
        <TaskForm />
        <TaskList />
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import Navbar from '../components/Navbar.vue';
  import ProfileForm from '../components/ProfileForm.vue';
  import ProfileList from '../components/ProfileList.vue';
  import TaskForm from '../components/TaskForm.vue';
  import TaskList from '../components/TaskList.vue';
  </script>
  