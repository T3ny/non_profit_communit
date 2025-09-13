import { useState } from "react";
import axios from "axios";

export default function Signup() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/users/signup/", form);
      localStorage.setItem("token", res.data.token);
      setMessage("Signup successful!");
    } catch (err) {
      setMessage(err.response?.data?.error || "Signup failed");
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "auto", marginTop: "50px" }}>
      <h2>Signup</h2>
      <div class = "container">
        <form onSubmit={handleSubmit}>
            <input name="username" placeholder="e.g John" value={form.username} onChange={handleChange} /><br/>
            <input name="email" placeholder="youexample@gm" value={form.email} onChange={handleChange} /><br/>
            <input type="password" name="password" placeholder="********" value={form.password} onChange={handleChange} /><br/>
            <input type="password" name="confirmpassword" placeholder="********" value={form.password} onChange={handleChange} /><br/>
            <button type="submit">Signup</button>
        </form>
      </div>
      <p>{message}</p>
    </div>
  );
}
