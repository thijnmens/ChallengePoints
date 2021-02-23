import express from 'express'
import userRoute from './routes/user'
import mapRote from './routes/maps'

const app = express()

app.use('/api/user', userRoute)
app.use('/api/maps', mapRote)
app.use('/Website', express.static('../Website'))

app.listen(80, () => {
    console.log('Listening on port 80')
})