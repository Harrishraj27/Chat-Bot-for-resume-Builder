<template>
  <div>
    <h1>Resume Builder</h1>
    <QuestionForm
      v-if="currentQuestion"
      :question="currentQuestion"
      @answered="handleAnswer"
    />
    <p v-else>Thank you! Your resume is being generated.</p>
  </div>
</template>

<script>
import QuestionForm from '@/components/QuestionForm.vue';

export default {
  components: {
    QuestionForm,
  },
  data() {
    return {
      currentQuestion: 'What is your full name?',
    };
  },
  methods: {
    async handleAnswer(output, nextQuestion) {
      if (nextQuestion === 'All questions completed. Thank you!') {
        this.currentQuestion = null;
        await this.generateResume();
      } else {
        this.currentQuestion = nextQuestion;
      }
    },
    async generateResume() {
      try {
        const response = await this.$axios.get('/generate_resume');
        window.open().document.write(response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
</style>
