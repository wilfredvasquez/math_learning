<template>
  <layout tabs-active="security">
    <template #settings-content>
      <security
        :session-expire-time="global_settings.timeExpiredSession"
        :success="success"
        :errors="errors"
      />
    </template>
  </layout>
</template>

<script>
import Layout from '@components/Layouts/LayoutGlobalSettings.vue'
import Security from './Security.vue'

export default {
  name: "SecurityIndex",
  components: {
    Layout,
    Security
  },
  props: {
    auth: {
      type: Object,
      default: () => { }
    },
    success: {
      type: Object,
      default: () => { }
    },
    errors: {
      type: Object,
      default: () => { }
    },
    global_settings: {
      type: Object,
      default: () => { }
    },
    auditInstalled: {
      type: Boolean,
      default: () => false
    }
  }
}
</script>
