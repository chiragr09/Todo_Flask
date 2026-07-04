import { defineConfig } from 'vite'
import react, { reactCompilerPreset } from '@vitejs/plugin-react'
import babel from '@rolldown/plugin-babel'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    babel({ presets: [reactCompilerPreset()] })
  ],
  build: { assetsDir: 'static' ,},
  server: {
    port: 3000,
    cors: true,
    proxy: {
      "/tasks": {
        target: "http://127.0.0.1:5000/",
        changeOrigin: true,
        secure: false,
      }
    }
  }
})
