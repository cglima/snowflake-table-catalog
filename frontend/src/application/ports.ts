import { Table } from '../domain/entities';

export interface TableRepository {
  getTables(): Promise<Table[]>;
}
