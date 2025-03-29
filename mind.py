import React, { useState, useEffect } from "react";
import "./App.css";

const motivationPrompts = [
  "Believe in yourself! You are capable of amazing things.",
  "Every day is a new beginning. Take a deep breath and start again.",
  "Success is the sum of small efforts, repeated daily.",
  "Keep going. Everything you need will come to you at the perfect time.",
  "Difficulties in life are intended to make us better, not bitter.",
  "You are stronger than you think. Keep pushing forward!",
  "Your potential is limitless. Never stop exploring your capabilities.",
  "The only way to achieve the impossible is to believe it is possible.",
  "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
  "You are capable, you are strong, and you can do this!"
];

const anxietyReliefPrompts = [
  "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
  "Close your eyes and picture your happy place. Stay there for a moment.",
  "Write down what’s bothering you and set it aside for later.",
  "Try progressive muscle relaxation – tense each muscle, then relax it.",
  "Listen to calming music or nature sounds to ease your mind.",
  "Step outside and take a short walk to clear your thoughts.",
  "Drink a warm cup of tea or water. Hydration helps relaxation.",
  "Focus on the present. What are five things you can see and hear?",
  "Talk to someone you trust about what’s making you anxious.",
  "Remind yourself: You have overcome challenges before, and you will again."
];

const studyTips = [
  "Use the Pomodoro technique – study for 25 mins, take a 5-min break.",
  "Teach what you learn to someone else. It helps retain information!",
  "Summarize notes in your own words to enhance understanding.",
  "Practice active recall – test yourself instead of rereading notes.",
  "Break large tasks into smaller chunks to avoid feeling overwhelmed.",
  "Use mnemonic devices to memorize complex concepts.",
  "Find a distraction-free study environment for better focus.",
  "Use visual aids like mind maps and diagrams to remember better.",
  "Get enough sleep! Rest is crucial for memory retention.",
  "Stay hydrated and take regular breaks to keep your mind fresh."
];

const selfCareTips = [
  "Take a 5-minute stretch break to ease your muscles.",
  "Maintain a good posture while studying to avoid back pain.",
  "Eat brain-boosting foods like nuts, fruits, and dark chocolate.",
  "Avoid excessive caffeine; try herbal tea instead.",
  "Get sunlight exposure to boost your mood and energy levels.",
  "Set realistic goals and celebrate small achievements.",
  "Listen to calming music while studying to reduce stress.",
  "Practice gratitude – write down three things you are grateful for.",
  "Take a deep breath and remind yourself it’s okay to take breaks.",
  "Limit screen time before bed to ensure better sleep quality."
];

const MindEase = () => {
  const [motivation, setMotivation] = useState("Click 'Inspire Me' for motivation!");
  const [anxiety, setAnxiety] = useState("Click 'Anxiety Relief' for help.");
  const [studyPlan, setStudyPlan] = useState([]);
  const [studyTimer, setStudyTimer] = useState(25);
  const [breakTime, setBreakTime] = useState(5);

  const generateStudyPlan = () => {
    let plan = [];
    for (let i = 1; i <= 3; i++) {
      plan.push(`📚 Subject ${i}: Study for ${(studyTimer / 3).toFixed(2)} mins`);
    }
    setStudyPlan(plan);
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>MindEase Tools</h2>
        <button onClick={() => setMotivation(motivationPrompts[Math.floor(Math.random() * motivationPrompts.length)])}>✨ Inspire Me!</button>
        <button onClick={() => setAnxiety(anxietyReliefPrompts[Math.floor(Math.random() * anxietyReliefPrompts.length)])}>🧘 Anxiety Relief</button>
        <button onClick={() => alert(studyTips[Math.floor(Math.random() * studyTips.length)])}>📖 Study Tips</button>
        <button onClick={() => alert(selfCareTips[Math.floor(Math.random() * selfCareTips.length)])}>💆 Self-Care</button>
      </aside>
      
      <main className="content">
        <h1>Welcome to MindEase!</h1>
        <h3>{motivation}</h3>
        <h3>{anxiety}</h3>
        
        <h2>Study Planner Generator</h2>
        <button onClick={generateStudyPlan}>📅 Generate Study Plan</button>
        <ul>{studyPlan.map((item, index) => <li key={index}>{item}</li>)}</ul>

        <h2>Daily Affirmation</h2>
        <p>{motivationPrompts[new Date().getDate() % motivationPrompts.length]}</p>

        <h2>Study Timer</h2>
        <input type="number" value={studyTimer} onChange={(e) => setStudyTimer(e.target.value)} /> min
        <input type="number" value={breakTime} onChange={(e) => setBreakTime(e.target.value)} /> min break
      </main>
    </div>
  );
};

export default MindEase;
