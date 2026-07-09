const express = require("express");
const axios = require("axios");

const app = express();

app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
    res.render("index");
});

app.post("/submit", async (req, res) => {

    try {

        const response = await axios.post(
            "http://127.0.0.1:5000/submit",
            req.body
        );

        res.send(response.data.message);

    } catch (err) {

        console.log(err);

        res.send("Backend Not Running");

    }

});

app.listen(3000, () => {
    console.log("Frontend Running");
});