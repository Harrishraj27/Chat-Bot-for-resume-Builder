<template>
  <div>
    <p>{{ question }}</p>
    <input v-model="answer" @keyup.enter="submitAnswer" placeholder="Type your answer and press enter" />
    <button @click="submitAnswer">Submit</button>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      answer: '',
      context: '',
    };
  },
  methods: {
    async submitAnswer() {
      try {
        const response = await this.$axios.post('/resume_bot', {
          context: this.context,
          question: this.answer,
        });
        this.$emit('answered', response.data.output, response.data.next_question);
        this.context += `\nUser: ${this.answer}\nAI: ${response.data.output}`;
        this.answer = '';
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
