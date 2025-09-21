import { Table } from '../domain/entities';
import { TableRepository } from './ports';

export class GetTables {
  constructor(private readonly tableRepository: TableRepository) {}

  async execute(): Promise<Table[]> {
    return this.tableRepository.getTables();
  }
}
