<script lang="ts" setup>
import { useEventData } from '../event.utils'
import { useAuthStore } from '@/stores/auth.store'

const authStore = useAuthStore()
const {
  events,
  handleAttendanceUpdate,
  countAttendees,
  totalAttendees,
  formatDate
} = useEventData()

</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title bg-dark-subtle fs-5">
      Upcomming Events
    </div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-sm border-light table-dark align-middle">
          <thead>
            <tr>
              <td scope="col" class="col-3">Confirmed</td>
              <td scope="col" class="col-6">Event Details</td>
              <td scope="col" class="col-3 text-center">Your Attendance</td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="event in events" :key="event.id">
              <td>
                {{ countAttendees(event.attendance) }} of
                {{ totalAttendees(event.attendance) }}
              </td>
              <td>
                <router-link
                  class="link-info link-underline-opacity-0"
                  to=""
                  data-bs-toggle="modal"
                  :data-bs-target="`#eventModal${event.id}`"
                  >{{ event.title }}</router-link
                >
                <div
                  class="modal fade"
                  :id="`eventModal${event.id}`"
                  tabindex="-1"
                  :aria-labelledby="`eventModalLabel${event.id}`"
                  aria-hidden="true"
                >
                  <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                      <div class="modal-header border-light">
                        <h1
                          class="modal-title fs-5"
                          :id="`eventModalLabel${event.id}`"
                        >
                          Verify Attendance
                        </h1>
                        <button
                          type="button"
                          class="btn btn-outline-secondary border-light"
                          data-bs-dismiss="modal"
                          aria-label="Close"
                        >
                          <font-awesome-icon
                            icon="fa-solid fa-xmark"
                            size="lg"
                          />
                        </button>
                      </div>
                      <div class="modal-body text-center">
                        <button
                          class="btn btn-success me-2"
                          data-bs-dismiss="modal"
                          @click="handleAttendanceUpdate(event.id, true)"
                        >
                          Yes <font-awesome-icon icon="fa-solid fa-thumbs-up" />
                        </button>
                        <button
                          class="btn btn-outline-danger"
                          @click="handleAttendanceUpdate(event.id, false)"
                          data-bs-dismiss="modal"
                        >
                          No
                          <font-awesome-icon icon="fa-solid fa-thumbs-down" />
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <p class="small mb-0">{{ formatDate(event.date) }}</p>
                <p class="small">{{ event.details }}</p>
              </td>
              <td class="text-center">
                {{ event.attendance[authStore.discord_id] ? 'Yes' : 'No' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
