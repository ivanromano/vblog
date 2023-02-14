import { model, Schema } from "mongoose";

const userSchema = new Schema({
  'email': {
    type: String
  },
  'name': {
    type: String
  },

})
export const User = model('User', userSchema)
// export default defineEventHandler(async (event) => {
//   const users = await User.find()

//   return {
//     users
//   }
// })