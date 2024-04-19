<script lang="ts">
	import { Projects } from "$lib/index";

	async function run_mdkp() {
		const resp = await fetch("/api/compute", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				config: {
					storage: "hard",
					memory: "hard",
					cpu_time: "hard",
					worker_time: "hard"
				},
				projects: $Projects
			}),
		});
		const json = await resp.json();
		console.log("output:", json);
	}

    function get_random(min: number, max: number) {
        return Math.floor(Math.random() * ((max-min)+1)) + min;
    }

    function add_project() {
        $Projects.push({
            storage: get_random(1, 10),
            memory: get_random(1, 10),
            cpu_time: get_random(1, 10),
            worker_time: get_random(1, 10),
            value: get_random(1, 10),
        });
        $Projects = $Projects;
    }

	if ($Projects.length == 0) {
		add_project();
	}
</script>

<button class="button" on:click={() => {console.log($Projects)}}>Print</button>

<button class="button" on:click={run_mdkp}>Run MDKP</button>
