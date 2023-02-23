import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
// /blog/full/?slug=pensante
export const useDjangoStore = defineStore("django", () => {
	const token = ref(null)
	const contenido = ref(null)
  const localhost = 'https://poison.onrender.com'
  const post = ref()
  const count = ref()
  const next = ref()
  const previous = ref()
  const vblog = ref([])
  const blog_slug = ref(null)
  const principal_categories = ref([])


  
  const categories = async () => {
  try {
    const res = await axios.get(`${localhost}/blog/cat`)
    principal_categories.value = res.data.categories.map((objeto, index) => {
      let subcategoryCounter = 0;
      const subcategories = objeto.sub_categories.map((subcategory) => {
        const newId = subcategoryCounter++;
        return {
          ...subcategory,
          new_id: newId
        };
      });

      return { ...objeto, sub_categories: subcategories, new_id: index };
    });

    // console.log(principal_categories.value);
  } catch (error) {
    console.log(error);
  } 
}

  const lista_blog = async () => {
    try {
      const res = await axios.get(`${localhost}/blog/posts`)
      
      vblog.value = res.data.results
      // console.log(vblog.value);
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

  const get_blog = async (slug = `moscas`) => {
    try {
      const res = await axios.get(`${localhost}/blog/${slug}`)
      return res.data
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
      // get_blog('moscas')
      categories()
      lista_blog()
	return {contenido,
          token,
          principal_categories,
          vblog,
          blog_slug,
          get_blog,
          categories, lista_blog,
          pagi_lista_blog,
          full_blog_category,
          full_blog_category_page,
          }
})