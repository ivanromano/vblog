import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
// /blog/full/?slug=pensante
export const useDjangoStore = defineStore("django", () => {
	const token = ref(null)
	const contenido = ref(null)
  const localhost = 'http://localhost:8000'
  const post = ref()
  const count = ref()
  const next = ref()
  const previous = ref()
  const principal_categories = ref([])
  const vblog = ref(null)

  const categories = async () => {
    try {
      const res = await axios.get(`${localhost}/blog/cat`)
      // console.log(res.data.categories);
      principal_categories.value = res.data.categories
    } catch (error) {
      console.log(error);
    } 
  }

  const lista_blog = async () => {
    try {
      const res = await axios.get(`${localhost}/blog/posts`)
      console.log(res.data.results);
      vblog.value = res.data.results
    } catch (error) {
      console.log(error);
    }
  }

  const pagi_lista_blog = async (page = 1) => {
    try {
      const res = await axios.get(`${localhost}/blog/posts?page=${page}`)
      console.log(res.data.results);
      
    } catch (error) {
      console.log(error);
    }
  }
	
  const full_blog_category = async (slug = 'pensante') => {
    try {
      const res = await axios.get(`${localhost}/blog/full/?slug=${slug}`)
      console.log(res.data.results);
      
    } catch (error) {
      console.log(error);
    }
  }

  const full_blog_category_page = async (slug = 'pensante', page = 1) => {
    try {
      const res = await axios.get(`${localhost}/blog/full/?slug=${slug}&page=${page}`)
      console.log(res.data.results);
      
    } catch (error) {
      console.log(error);
    }
  }

  const get_blog = async (slug = 'pensante') => {
    try {
      const res = await axios.get(`${localhost}/blog/?slug=${slug}`)
      console.log(res.data.results);
      
    } catch (error) {
      console.log(error);
    }
  }

	const register = async (email, password, name) => {
		    try {
		      console.log("hiciste click");
		      const res = await axios.post("http://127.0.0.1:8000/users/create", {
		        email: email,
		        password: password,
		        name: name,
		      });
		      console.log(res.data);
		      localStorage.setItem('user', 'vas a necesitar mas que eso para hackearme :)')
		    } catch (error) {
		      if (error.response) {
		        throw error.response.data
		      } else if (error.request) {
		        console.log(error.request);
		      } else {
		        // Algo paso al preparar la petición que lanzo un Error
		        console.log('Error', error.response.data);
		      }
		    }
		  }
			

      // full_blog_category('pensante')
      categories()
      lista_blog()
	return {contenido,
          token,
          principal_categories,
          vblog,
          categories, lista_blog,
          pagi_lista_blog,
          full_blog_category,
          full_blog_category_page,
          }
})