const amqp= require('amqlib')
const readline = require ('readline')


async function startUserA(){

    const connection= await amqp.connection('amqp://localhost')
    const channel = await connection.createChannel();
    const exchange = 'direct_exchange'
    const queue = userA_queue
    
    await channel.assertExchange(exchange(exchange, 'direct', {durable :false}))
    await channel.assertQueue(queue, { durable:false})
    await channel.bindQueue(queue, exchange, "userB_key")
    

    



}