import { ref } from 'vue'

export function getEntities(url: string) {
  const response = ref()
  const status = ref()

  const request = async () => {
    const result = await fetch(url)

    status.value = result.status
    response.value = await result.json()
  }

  return { response, request, status }
}
