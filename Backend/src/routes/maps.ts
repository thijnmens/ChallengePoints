import express from 'express'

import firebase from 'firebase'
import '../firebaseinnit'
var db = firebase.firestore()

const router = express.Router()

router.get('/:mapHash/map', async (req, res, next) => {
    var data = await db.collection('maps').doc(req.params.mapHash).get()
    if (!data.exists) { res.sendStatus(404); return; }

    res.send(data.data())
})

router.get('/:mapHash/scores', async (req, res, next) => {
    var data = await db.collection('map-scores').doc(req.params.mapHash).get()
    if (!data.exists) { res.sendStatus(404); return; }

    var mapData = data.data()
    mapData.hash = data.id

    res.send(mapData)
})

router.get('/all', async (req, res) => {
    var data = await db.collection('maps').get()
    var maps = []

    for (const i of data.docs) {
        var mapData = i.data()
        mapData.hash = i.id
        mapData.cover = `https://firebasestorage.googleapis.com/v0/b/challenge-points-dev.appspot.com/o/map-covers%2F${i.id}.jpg?alt=media&token=ee595d97-4b34-414a-aede-fbdb52e490f1`
        maps.push(mapData)
    }

    res.send(maps)
})

export default router