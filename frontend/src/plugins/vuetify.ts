import { createVuetify, ThemeDefinition } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";


const myCustomLightTheme = {
  dark: false,
  colors: {
    background: '#FFFFFF',
    surface: '#FFFFFF',
    primary: '#6200EE',
    'primary-darken-1': '#3700B3',
    secondary: '#03DAC6',
    'secondary-darken-1': '#018786',
    error: '#B00020',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
    vicYellow: '#FFCC67',
    'vicYellow-darken-1': '#fff',
    vicOrange: '#FF9557',
    vicPink: '#F95794',
    vicPink2: '#FF1557',
    vicBlue: '#A3D858',
    vicRed: '#E52E71',
    grass: '#33b841',
    fire: '#f52f44',
    flying: '#2196F3',
    water: '#5578d9',
    bug: '#68ad26',
    normal: '#9c9b9a',
    electric: '#FB8C00',
    ground: '#805f12',
    fairy: '#c740a5',
    fighting: '#c74d22',
    psychic: '#ab3067',
    rock: '#797d39',
    steel: '#4e7273',
    ice: '#29a9ab',
    ghost: '#6b3d73',
    dark: '#1c1f2e',
    // grass: '#2fed49',
    poison: '#6200EE',

  }
}

export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    components,
    directives,
    theme: {
      defaultTheme: 'myCustomLightTheme',
      themes: {
        myCustomLightTheme,
      }
    }
  })
  nuxtApp.vueApp.use(vuetify)
})