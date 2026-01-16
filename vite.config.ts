import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    base: './',
    server: {
        host: '0.0.0.0', // Allow access from other devices on the network
        port: 5173,
    },
})
