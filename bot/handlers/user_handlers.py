import asyncio
from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

user_router = Router()

class UserForm(StatesGroup):
    waiting_for_name = State()

@user_router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    """Processes the `/start` message"""
    await msg.answer(
        text = f"Hello {hbold(msg.from_user.first_name)}!"
    )


@user_router.message(Command("set_name"))
async def set_name(msg: types.Message, state: FSMContext) -> None:
    await state.set_state(UserForm.waiting_for_name)
    await msg.answer(
        text="How should I call you?"
    )


@user_router.message(UserForm.waiting_for_name)
async def process_name(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(name=msg.text)
    await msg.answer(
        text=f"Nice to meet you, {msg.text}!"
    )
    # TODO: add saving to a DB
    await state.clear()


@user_router.message(F.text)
async def answer_text_message(msg: types.Message) -> None:
    """Answers to a text message."""
    thinking_message: types.Message = await msg.reply(
        text = "Analyzing your text..."
    )
    await asyncio.sleep(3)
    answer_text = f"Finished analyzing! Length: {len(msg.text)} symbols, {len(msg.text.split())} words."
    # TODO: add API calls
    
    await thinking_message.edit_text(
        text=answer_text
    )


@user_router.message(F.document)
async def answer_document_message(msg: types.Message) -> None:
    """Answers to a document message."""
    file_name: str = msg.document.file_name or "unknown"
    file_size: int = msg.document.file_size
    file_caption: str = msg.caption or ""
    caption_length = len(file_caption)
    caption_length_msg = f"Caption lenght: {caption_length}"

    thinking_message: types.Message = await msg.reply(
        text="Analyzing your document..."
    )

    if not file_name.lower().endswith(".pdf"):
        await thinking_message.edit_text(
            text="Not a PDF document!" + caption_length_msg
        )
        return

    await asyncio.sleep(3)
    answer_text = f"Document '{file_name}' ({file_size} bytes) was successfully processes by our mock AI."
    # TODO: add API calls
    
    await thinking_message.edit_text(
        text=f"{answer_text}\n{caption_length_msg}"
    )