import './assets/main.scss'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { applyColors } from './color_funcs'

const app = createApp(App)

app.use(router)

app.mount('#app')
applyColors()