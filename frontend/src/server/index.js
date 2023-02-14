import { Nitro } from "nitropack";
import mongoose from 'mongoose';

export default async (_nitro_app) => {
  const config = useRuntimeConfig()
  console.log('hol');
  
  try {
    await mongoose.connect(config.MONGODB_URI)
    console.log('conectado a mongodb');
  } catch (error) {
    // console.log(error.message);
    
  }
}