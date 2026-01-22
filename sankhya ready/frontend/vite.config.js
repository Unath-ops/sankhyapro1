import { fileURLToPath, URL } from 'url';
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
    logLevel: 'error',
    build: {
        emptyOutDir: true,
        sourcemap: false,
        minify: false
    },
    css: {
        postcss: './postcss.config.js'
    },
    plugins: [
        react()
    ],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
        },
    }
});
