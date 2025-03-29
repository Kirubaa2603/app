import React, { useState } from "react";

const motivationPrompts = [
  "You are stronger than you think! 💪",
  "Every small step matters. Keep going! 🚀",
  "Believe in yourself; you are capable! 🌟",
  "Success is built on consistency. Stay at it! 🔥",
  "You’ve got this! Trust the process. 💙",
  "Difficulties are just stepping stones to success. 🌈",
  "One day, you'll look back and be proud. ✨",
  "Your future self will thank you for today’s effort! 🙌",
  "Keep moving forward, even if it's just a little. 🌱",
  "Hard work always pays off. You are amazing! 🎯",
];

const anxietyPrompts = [
  "Breathe deeply; you are safe. 🌿",
  "Your feelings are valid, but they don’t define you. 💙",
  "Close your eyes and focus on slow breaths. 🌬️",
  "Anxiety is temporary. This moment will pass. ⏳",
  "You are in control of your thoughts. 🧠",
  "Shift your focus to things you can control. 🎯",
  "Tense and relax your muscles. Feel the relief. ☁️",
  "Visualize a peaceful place. 🏞️",
  "Your mind is powerful, and you are stronger. 💖",
  "You deserve calm and peace. 💫",
];

const studyTips = [
  "Use the Feynman Technique: Explain it like you're teaching a child. 👨‍🏫",
  "Use the Pomodoro technique: 25 mins study, 5 mins break. 🍅",
  "Take handwritten notes to improve memory. ✍️",
  "Summarize key points after each study session. 📖",
  "Try active recall instead of passive reading. 🔄",
  "Practice spaced repetition for long-term memory. ⏳",
  "Study in a distraction-free zone. 🚫📱",
  "Drink water and stay hydrated. 💧",
  "Sleep well to retain what you study. 💤",
  "Use mnemonic techniques for tough topics. 🎭",
];

const selfCareTips = [
  "Stretch for 5 minutes to release tension. 🧘",
  "Step outside and get fresh air. 🌿",
  "Listen to calming music while studying. 🎶",
  "Close your eyes for a minute and relax. 🌸",
  "Massage your temples if you feel stressed. 🤲",
  "Take deep breaths and reset your focus. 🌬️",
  "Write down what’s stressing you and let it go. ✍️",
  "Eat a healthy snack to refuel your brain. 🍎",
  "Stay hydrated; your brain needs water! 💦",
  "Celebrate small wins. You are doing great! 🎉",
];

const emotions = {
  Happy: "Your joy is contagious! Keep spreading positivity! 🌞",
  Sad: "You are not alone. Better days are ahead. 💙",
  Anxious: "Breathe in, breathe out. You’re stronger than this moment. 🌿",
  Stressed: "Take a deep breath. Small steps, one at a time. 💆‍♂️",
  Excited: "Embrace the excitement! Let’s make today amazing! 🚀",
  Motivated: "Ride the wave of motivation and go for your dreams! 🌟",
  Tired: "Take a break. Rest is productive too. 🌙",
  Confident: "You’re unstoppable! Keep that energy going. 🔥",
  Overwhelmed: "Pause, prioritize, and proceed. You got this! 📌",
};

const App = () => {
  const [selectedTab, setSelectedTab] = useState("Motivation");
  const [emotion, setEmotion] = useState("");
  const [studySubjects, setStudySubjects] = useState(1);
  const [studyPlan, setStudyPlan] = useState([]);
  const [studyTime, setStudyTime] = useState(30);
  const [breakTime, setBreakTime] = useState(5);

  const generateStudyPlan = () => {
    let plan = [];
    for (let i = 0; i < studySubjects; i++) {
      plan.push(`📚 Subject ${i + 1}: Study for ${studyTime / studySubjects} mins`);
    }
    plan.push(`☕ Break for ${breakTime} mins`);
    setStudyPlan(plan);
  };

  return (
    <div className="flex min-h-screen bg-blue-50 text-gray-800">
      {/* Sidebar */}
      <div className="w-1/4 bg-blue-100 p-6 shadow-md">
        <h2 className="text-2xl font-bold">💙 MindEase Tools</h2>
        <div className="mt-4 space-y-3">
          {["Motivation", "Study Tips", "Self-Care"].map((tab) => (
            <button
              key={tab}
              onClick={() => setSelectedTab(tab)}
              className={`block w-full text-left p-2 rounded ${
                selectedTab === tab ? "bg-blue-400 text-white" : "bg-blue-200"
              }`}
            >
              {tab}
            </button>
          ))}
        </div>
      </div>

      {/* Main Content */}
      <div className="w-3/4 p-6">
        <h1 className="text-3xl font-bold">🌿 Welcome to MindEase Tools</h1>

        {/* Emotion Dropdown */}
        <h2 className="mt-6">How do you feel today?</h2>
        <select onChange={(e) => setEmotion(e.target.value)} className="p-2 border rounded">
          <option value="">Select Emotion</option>
          {Object.keys(emotions).map((emo) => (
            <option key={emo} value={emo}>
              {emo}
            </option>
          ))}
        </select>
        {emotion && <p className="mt-2 p-3 bg-blue-200 rounded">{emotions[emotion]}</p>}

        {/* Study Planner */}
        <h2 className="mt-6">📖 Study Planner Generator</h2>
        <input
          type="number"
          min="1"
          value={studySubjects}
          onChange={(e) => setStudySubjects(e.target.value)}
          className="border p-2"
        />
        <button onClick={generateStudyPlan} className="ml-2 bg-blue-400 p-2 rounded text-white">
          Generate Plan
        </button>
        {studyPlan.length > 0 && (
          <ul className="mt-2 p-3 bg-blue-200 rounded">
            {studyPlan.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        )}

        {/* Dynamic Section */}
        <div className="mt-6 p-3 bg-blue-100 rounded">
          {selectedTab === "Motivation" && <p>{motivationPrompts[Math.floor(Math.random() * 10)]}</p>}
          {selectedTab === "Study Tips" && <p>{studyTips[Math.floor(Math.random() * 10)]}</p>}
          {selectedTab === "Self-Care" && <p>{selfCareTips[Math.floor(Math.random() * 10)]}</p>}
        </div>
      </div>
    </div>
  );
};

export default App;
