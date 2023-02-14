export async function registerWithEmail(username, name, email, password) {
  try {
    const res = await $fetch('api/auth/register', {
      method: 'POST',
      body: {username, name, email, password}
    })

    if (res) {
      useState('user').value = res
      await useRouter().push('/')
    }
  } catch (error) {
    console.log('error: ' + error.toString());
    
  }
}
