import React from "react";

import axios from "axios";
import { useState } from "react";
const Home = () => {
  const [img, setImg] = useState();
  const [height, setHeight] = useState();
  const [width, setWidth] = useState();

  const sendImg = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("image", img);
    const res = await axios.post("http://localhost:5000/grayscale", formData);
    console.log(res);
  };

  const resize = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("image", img);
    formData.append("height", height);
    formData.append("width", width);
    const res = await axios.post("http://localhost:5000/resize", formData);
    console.log(res);
  };

  const rotate = async (e,rotateAngle) => {
    e.preventDefault();
    console.log(rotateAngle)
    const formData = new FormData();
    formData.append("image", img);
    formData.append("rotate", rotateAngle);
    
    const res = await axios.post("http://localhost:5000/rotateAngle", formData);
    console.log(res);
  }

  
  return (
    <>
      <div className=" flex justify-center items-center mt-10">
        <div class="shrink-0">
          <img
            class="h-16 w-16 object-cover rounded-full"
            src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1361&q=80"
            alt="Current profile photo"
          />
        </div>
        <label class="block">
          <span class="sr-only">Choose profile photo</span>
          <input
            type="file"
            onChange={(e) => setImg(e.target.files[0])}
            class="block w-full text-sm text-slate-500
      file:mr-4 file:py-2 file:px-4
      file:rounded-full file:border-0
      file:text-sm file:font-semibold
      file:bg-violet-50 file:text-violet-700
      hover:file:bg-violet-100
    "
          />
        </label>
      </div>
      <div className=" flex justify-center items-center mt-10">
        <div
          className="py-2.5 px-5 border rounded-xl bg-violet-700 text-white text-2xl cursor-pointer active:scale-95"
          onClick={sendImg}
        >
          Change image to grayscale
        </div>
      </div>
      <div className=" flex justify-center items-center mt-10">
        <div className="py-2.5 px-5 border rounded-xl bg-violet-700 text-white text-2xl cursor-pointer active:scale-95 flex  gap-2">
          <input
            type="number"
            name=""
            id=""
            capture
            className="h-16 w-32 text-black flex justify-center items-center "
            placeholder="height(px)"
            value={height}
            onChange={(e) => setHeight(e.target.value)}
          />
          <input
            type="number"
            name=""
            id=""
            capture
            className="h-16 w-32 text-black flex justify-center items-center"
            placeholder="width(px)"
            value={width}
            onChange={(e) => setWidth(e.target.value)}
          />
        </div>
      </div>
      <div className=" flex justify-center items-center mt-10">
        <div
          className="py-2.5 px-5 border rounded-xl bg-violet-700 text-white text-2xl cursor-pointer active:scale-95"
          onClick={resize}
        >
          resize image 
        </div>
      </div>

      <div className=" flex justify-center items-center mt-10">
        <div className="py-2.5 px-5 border rounded-xl bg-violet-700 text-white text-2xl cursor-pointer active:scale-95 flex  gap-2" onClick={(e) => rotate(e,-1)}>
          Flip-X{" "}
        </div>
        <div className="py-2.5 px-5 border rounded-xl bg-violet-700 text-white text-2xl cursor-pointer active:scale-95 flex  gap-2" onClick={(e) => rotate(e,0)}>
          Flip 180{" "}
        </div>
        <div className="py-2.5 px-5 border rounded-xl bg-violet-700 text-white text-2xl cursor-pointer active:scale-95 flex  gap-2" onClick={(e) => rotate(e,1)}>
          Flip 180-X{" "}
        </div>
      </div>
    </>
  );
};

export default Home;
