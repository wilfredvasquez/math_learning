<template>
  <layout tabs-active="general">
    <template #settings-content>
      <appearance
        :app-name="global_settings.appName"
        :app-logo="global_settings.appLogo"
        :success="success"
        :errors="errors"
      />

      <registration
        :success="success"
        :errors="errors"
        :registration-active="global_settings.activeRegistration"
      />
    </template>
  </layout>
</template>

<script>
import Layout from '@components/Layouts/LayoutGlobalSettings.vue'
import Appearance from './Appearance.vue'
import Registration from './Registration.vue'

export default {
  name: 'GeneralIndex',
  components: {
    Layout,
    Appearance,
    Registration,
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
  }
}
</script>
