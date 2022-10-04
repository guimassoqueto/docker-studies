import express, { Express, Request, Response } from "express";

const app: Express = express();
const port: number = Number.parseInt(process.env.PORT!);

app.get("/", (req: Request, res: Response) => {
    res.send("<h1>Hello World</h1>")
})

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`)
})