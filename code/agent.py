import os, asyncio
from browser_use import Agent, ChatBrowserUse, BrowserSession

os.environ["BROWSER_USE_API_KEY"] = ""

async def main():
    session = BrowserSession(
        headless=False,
        user_data_dir=r"C:\Users\Lenovo\cellmate-lab\browser-profile",
        keep_alive=True,
    )
    agent = Agent(
        task=(
            "Открой https://gitlab.com/users/sign_in. НЕ заполняй форму сам и "
            "НЕ завершай задачу. Подожди 180 секунд — пользователь сейчас "
            "войдёт вручную в этом окне браузера. После ожидания проверь, "
            "залогинен ли ты. Если залогинен — открой "
            "https://gitlab.com/kalmykov0207/cellmate-project/-/issues и "
            "выполни каждый issue, результат запиши в отчёт."
        ),
        llm=ChatBrowserUse(model="bu-latest"),
        browser_session=session,
    )
    await agent.run()

asyncio.run(main())
