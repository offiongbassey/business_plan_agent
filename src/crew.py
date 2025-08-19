from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from src.tools.custom_tool import SerperTool

@CrewBase
class BusinessPlan():
    """BusinessPlan crew (Research → Modeling → Plan)"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def research_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['research_strategist'], # type: ignore[index]
            verbose=True,
            tools=[SerperTool()],  # Attach Serper search tool here
            allow_delegation=False

        )
    @agent
    def business_architect(self) -> Agent:
        return Agent(
            config=self.agents_config["business_architect"],  # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )

    @agent
    def venture_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["venture_writer"],  # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"],  # type: ignore[index]
            # The research output becomes context for modeling
        )

    @task
    def business_modeling_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_modeling_task"],  # type: ignore[index]
            # This consumes research context; its output feeds the plan writer
            context=[self.market_research_task()]  # type: ignore[list-item]
        )
    
    @task
    def business_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_plan_task"],  # type: ignore[index]
            output_file="{business_name}_business_plan.md",
            context=[self.market_research_task(), self.business_modeling_task()]  # type: ignore[list-item]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BusinessPlan crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Research → Plan Writing
            verbose=True,
        )