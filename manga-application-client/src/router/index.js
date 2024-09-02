import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: () => import('@/views/CatalogView.vue')
    },
    {
      path: '/title/:id',
      name: 'title',
      component: () => import('@/views/TitleView.vue')
    },
    {
      path: '/user/:id',
      name: 'user',
      component: () => import('@/views/UserView.vue')
    },
    {
      path: '/profile',
      name: 'userProfile',
      component: () => import('@/views/UserView.vue')
    },
    {
      path: '/create/title',
      name: 'CreateMangaForm',
      component: () => import('@/views/forms/createForms/CreateTitleForm.vue')
    }
  ]
})

export default router
