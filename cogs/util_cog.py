from asyncio import sleep
from random import randint

from discord import Interaction, Message, ui, ButtonStyle, Embed
from discord.app_commands import command, describe, Group
from discord.ext.commands import Bot, Cog



class DiceActionView(ui.View):
    @ui.button(label='한번 더 굴리기')
    async def roll_again(self, ctx: Interaction, button: ui.Button):
        view = DiceActionView()
        await ctx.response.send_message(randint(1,6), view=view)
        
        self.stop()
        await view.wait()
        await ctx.edit_original_response(view=None)
        
    @ui.button(label='한번 더 굴리기', style=ButtonStyle.blurple)
    async def roll_again_2(self, ctx: Interaction, button: ui.Button):
        view = DiceActionView()
        await ctx.response.send_message(randint(1,6), view=view)
        
        self.stop()
        await view.wait()
        await ctx.edit_original_response(view=None)



class UtilCog(Cog):
    util_group = Group(name='util', description='유틸리티 관련 커맨드')
               
    @Cog.listener()
    async def on_message(self, message: Message):
        print(f'메시지가 입력됨! {message.id}: {message.content}')
    
    @util_group.command(description='pong이라고 보내줍니다.')
    async def ping(self, ctx: Interaction):
        await ctx.response.send_message(':ping_pong: Pong!')
        
    @util_group.command(description='보낸 메시지를 그대로 다시 돌려줍니다.')
    @describe(message='다시 돌려줄 메시지')
    async def echo(self, ctx: Interaction, message: str):
        await ctx.response.send_message(message)
            
    @command()
    async def add(self, ctx: Interaction, a: int, b: int):
        await ctx.response.send_message(f'{a} + {b} = {a+b}')
        
    @util_group.command(description='1부터 6까지 수 중 하나를 보여줍니다.')
    async def dice(self, ctx: Interaction):
        view = DiceActionView()
        await ctx.response.send_message(randint(1,6), view=view)
        await view.wait()
        
        await ctx.edit_original_response(view=None)
        
    @util_group.command(description='오래 걸리는 명령어')
    async def defers(self, ctx: Interaction):
        await ctx.response.defer()
        await sleep(5)
        await ctx.edit_original_response(content='명령어 실행 성공!')
        
        
    @util_group.command(description='임베드')
    async def embed(self, ctx: Interaction):
        embed = Embed(colour=0x4287f5, title='This is title', description='This is description')
        embed.add_field(name='메시지 보낸 사람 ID', value=f'{ctx.user.name}')
        embed.set_image(url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
        await ctx.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(UtilCog())