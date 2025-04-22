import { createRouter, createWebHistory } from 'vue-router'
import Login from '../pages/Login.vue'
import Dashboard from '../pages/Dashboard.vue'
import ProfileList from '../components/ProfileList.vue'
import ProfileForm from '../components/ProfileForm.vue'
import TaskList from '../components/TaskList.vue'
import TaskForm from '../components/TaskForm.vue'

const routes = [
  { path: '/', component: Login },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/profiles', component: ProfileList, meta: { requiresAuth: true } },
  { path: '/create-profile', component: ProfileForm, meta: { requiresAuth: true }, name: 'CreateProfile' },
  { path: '/profiles/edit/:id', component: ProfileForm, meta: { requiresAuth: true }, name: 'EditProfile' },  // Edited this line to add name
  { path: '/tasks', component: TaskList, meta: { requiresAuth: true } },
  { path: '/create-task', component: TaskForm, meta: { requiresAuth: true } },
  { path: '/tasks/edit/:id', component: TaskForm, meta: { requiresAuth: true }, name: 'EditTask' }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, _, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next('/')
  } else {
    next()
  }
})

export default router
