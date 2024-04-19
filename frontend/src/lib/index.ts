import { writable } from "svelte/store";
import type { ProjectInfo } from "../components/ProjectEntry";

export const Projects = writable<ProjectInfo[]>([]);
