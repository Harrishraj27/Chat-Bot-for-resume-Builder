<template>
  <div>
    <h2>{{ currentQuestion }}</h2>
    <form @submit.prevent="submitAnswer">
      <input v-model="answer" type="text" placeholder="Your answer" required />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      answer: '',
      currentQuestion: 'What is your full name?',
      context: '',
    };
  },
  methods: {
    async submitAnswer() {
      try {
        const response = await this.$axios.$post('http://127.0.0.1:8000/resume_bot', {
          context: this.context,
          question: this.answer,
        });
        this.context += `\nQ: ${this.currentQuestion}\nA: ${this.answer}`;
        this.answer = '';
        this.currentQuestion = response.next_question;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
input {
  margin-bottom: 10px;
  padding: 8px;
}
button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>
