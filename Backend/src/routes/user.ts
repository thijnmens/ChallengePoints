import express from 'express'

import firebase from 'firebase'
import '../firebaseinnit'
var db = firebase.firestore()

const router = express.Router()

router.get('/:userId/user', async (req, res, next) => {
    var data = await db.collection('users').doc(req.params.userId).get()
    if (!data.exists) { res.sendStatus(404); return; }

    res.send(data.data())
})

router.get('/:userId/scores', async (req, res, next) => {
    var data = await db.collection('user-scores').doc(req.params.userId).get()
    if (!data.exists) { res.sendStatus(404); return; }

    res.send(data.data())
})

export default router