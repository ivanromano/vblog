import { defineConfig } from 'windicss/helpers'

// import formsPlugin from 'windicss/plugin/forms'


export default defineConfig({
  shortcuts: {
    'btn': 'py-2 px-4 font-semibold rounded-lg shadow-md',
    'btn-green': 'text-white bg-red-500 hover:bg-green-700',
    'vic-btn': 'relative inline-flex items-center justify-center p-0.5 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg transform group bg-[#00DC82] group-hover:(from-cyan-500 to-blue-500) hover:(translate-y-1 text-white) focus:(ring-[5px] outline-none ring-cyan-200) duration-300',
    'vic-btn-span': 'font-medium relative px-5 py-2.5 transition-all ease-in duration-200 bg-[#00DC82] hover:(bg-light-50 text-[#00DC82]) rounded-md ',
    'vic-img-carousel': ' rounded-md transform hover:scale-110 group-hover:scale-[1.1] duration-300',
    'antSliderLink': 'bg-[#c96e3c] border border-[#df9638] py-[0px]',
    'antSliderLink2': 'bg-[#c96e3c] py-[1px]',
    'vic-slider': 'flex items-center duration-1000 group hover:(bg-blue-200 duration-700 text-blue-800) p-2 space-x-3 rounded-md',
    'vic-slider-span': 'text-gray-100 font-semibold duration-1000 transform group-hover:(text-blue-800 duration-500)',
    'input_normal': 'rounded-full relative flex-auto min-w-0 block w-full px-3 py-1.5 text-gray-700 bg-white bg-clip-padding border border-solid border-blue-300 rounded transition ease-in-out m-0 focus:outline-none',
    'navbar_link': 'w-full md:w-auto p-5 inline-block border-b-4 border-transparent hover:border-white duration-500'
  },
  // plugins: [formsPlugin],
})