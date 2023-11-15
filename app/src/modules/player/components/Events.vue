<script lang="ts" setup></script>

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
            <tr>
              <td>4 of 4</td>
              <td>
                <router-link class="link-info link-underline-opacity-0" to=""
                  >Game Session</router-link
                >
                <p class="small mb-0">November 18, 2023 @ 20:00 PM Central</p>
                <p class="small">Created By: J. Schmidt</p>
              </td>
              <td class="text-center">Yes</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
