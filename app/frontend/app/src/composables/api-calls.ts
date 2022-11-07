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

export function createEntities(url: string, data: object) {
  const response = ref()
  const status = ref()

  const request = async () => {
    const result = await fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })

    status.value = result.status
    response.value = result.json()
  }

  return { response, request, status }
}
