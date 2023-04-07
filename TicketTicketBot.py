import discord

intents = discord.Intents().all() # Enable all intents

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('!BuyRole'):
        # Get the category where the ticket channels should be created
        category_name = 'Premuim Tickets being Bought'
        category = discord.utils.get(message.guild.categories, name=category_name)

        # Create the ticket channel in the specified category
        channel_name = 'ticket-' + message.author.name
        channel = await category.create_text_channel(name=channel_name)

        # Create the role for members who should have access to the ticket channel
        ticket_access_role = await message.guild.create_role(name='Premuim Tickets being Bought')

        # Set the permissions of the ticket channel to only allow members with the ticket access role to see it
        await channel.set_permissions(ticket_access_role, read_messages=True)

        # Add the ticket access role to the member who created the ticket channel
        await message.author.add_roles(ticket_access_role)

        # Send the ticket creation message
        await channel.send('Hello Send 100K+owo cash/1+ Dollars, {}! And @Playing Roblox Will get Here As Fast As possible The role you will be getting is @Premuim 💎 Role.'.format(message.author.mention))
        # Delete the original message
        await message.delete()

    elif message.content.startswith('ok'):
        await message.channel.send('Ok Send The Money Here: https://paypal.me/SaifElabd Or do owo give @Mr.Saif 100000 Until @Mr.Saif Sees The Transaction you will not get your role.')
    
    elif message.content.startswith('!close'):
        if isinstance(message.channel, discord.TextChannel) and message.channel.name.startswith('ticket-'):
            await message.channel.delete()
        else:
            await message.channel.send('This command can only be used in a ticket channel.')

client.run('MTA5MzU3Nzk4Mjk3MjUzNDgwNA.GSiB-0.UHZq6cFr2J9zW82HX7rfQjUyQK5oz33mRAcoFE')