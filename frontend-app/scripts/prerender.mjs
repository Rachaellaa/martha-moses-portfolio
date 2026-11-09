import { createServer } from 'vite'
import { readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'

const root = process.cwd()

const server = await createServer({
  configFile: path.resolve(root, 'vite.config.ts'),
  server: {
    middlewareMode: true,
  },
  appType: 'custom',
})

try {
  const { render } = await server.ssrLoadModule('/src/entry-server.tsx')

  const template = await readFile(
    path.resolve(root, 'dist/index.html'),
    'utf-8'
  )

  const appHtml = render()

  const html = template.replace(
    '<div id="root"></div>',
    `<div id="root">${appHtml}</div>`
  )

  await writeFile(
    path.resolve(root, 'dist/index.html'),
    html,
    'utf-8'
  )

  console.log('Prerendering completed successfully.')
} finally {
  await server.close()
}